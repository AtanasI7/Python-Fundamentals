class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.collection = list()
        self.special_collection = list()

    def add_product(self, product_name: str):
        self.collection.append(product_name)

    def get_by_letter(self, first_letter: str):
        for i in self.collection:
            if i[0] == 'C':
                self.special_collection.append(i)
        return self.special_collection

    def __repr__(self):
        print(f"Items in the {self.name} catalogue:")
        self.collection = sorted(self.collection)
        for i in self.collection:
            print(i)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)