class TreeStore:
    def __init__(self, items):
        self.items = {}
        self.root = None

        # Создаем словарь для быстрого доступа к элементам
        for item in items:
            self.items[item['id']] = item
            if item['parent'] == 'root':
                self.root = item['id']

        # Создаем словарь для быстрого доступа к родителям
        self.parents = {item['id']: item['parent'] for item in items}

    def getAll(self) -> list:
        """
        Возвращает начальный массив элементов
        :return:
        """
        return list(self.items.values())

    def getItem(self, id) -> dict:
        """
        Возвращает объект с заданным идентификатором
        :param id: Идентификатор элемента
        :return:
        """
        return self.items[id]

    def getChildren(self, id) -> list:
        """
        Возвращает все дочерние элементы для заданного элемента
        :param id: Идентификатор элемента
        :return:
        """
        children_ids = [child_id for child_id, parent_id in self.parents.items() if parent_id == id]
        return [self.items[child_id] for child_id in children_ids]

    def getAllParents(self, id) -> list:
        """
        Возвращает цепочку родительских элементов для переданного элемента до корневого элемента
        :param id: Идентификатор элемента
        :return:
        """
        parents = []
        current_id = id
        current_id = self.parents[current_id]
        while current_id != self.root:
            parents.append(self.items[current_id])
            current_id = self.parents[current_id]
        parents.append(self.items[self.root])
        return parents
