from decimal import Decimal
from django.conf import settings
from store.models import Realty


class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        realty_ids = self.cart.keys()
        # получение объектов realty и добавление их в корзину
        realties = Realty.objects.filter(id__in=realty_ids)
        for realty in realties:
            self.cart[str(realty.id)]['realty'] = realty

        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item
        
    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, realty, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        realty_id = str(realty.id)
        if realty_id not in self.cart:
            self.cart[realty_id] = {'quantity': 0,
                                      'cost': str(realty.cost)}
        if update_quantity:
            self.cart[realty_id]['quantity'] = quantity
        else:
            self.cart[realty_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, realty):
        """
        Удаляем товар
        """
        realty_id = str(realty.id)
        if realty_id in self.cart:
            del self.cart[realty_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        print(self.cart.values())
        return sum(Decimal(item['cost']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()