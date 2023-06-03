from object_serializer import SerializerFactory
class Hello:
    @classmethod
    def test_classmethod(cls):
        return cls.__test


serializer = SerializerFactory.create_serializer("JSON")

ser = serializer.dumps(Hello)
print(ser)

des = serializer.loads(ser)

instance = des()
