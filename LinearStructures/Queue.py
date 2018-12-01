#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 12/1/18


class NodeForQueue:
    """
    Вспомогательный класс
    ухел очереди
    """
    def __init__(self, item=None):
        self.item = item  # нагрузка (значение) элемента
        self.next = None  # ссылка на следующий в очереди


class Queue:
    """
    Очередь
    """
    def __init__(self):
        """
        конструктор
        """
        self.m_front = None  # первый элемент
        self.m_back = None  # послдений элемент
        self.size = 0  # длина очереди

    def empty(self):
        """

        :return: True - если очередь пуста / False - в противном случае
        """
        return self.m_front is None and self.m_back is None

    def push(self, item):
        """
        добавляет элемент в очередь
        :param item: элемент
        :return:
        """
        self.size += 1
        new_node = NodeForQueue(item)
        if self.empty():
            self.m_front = new_node
        else:
            self.m_back.next = new_node
        self.m_back = new_node

    def pop(self):
        """
        Извлечь элемент из очереди
        :return: первый элемент в очереди
        """
        assert not self.empty(), 'Queue is empty!'
        current_front = self.m_front
        item = current_front.item
        self.m_front = self.m_front.next
        del current_front
        self.size -= 1
        if self.m_front is None:
            self.m_back = None
        return item

    def front(self):
        """
        возвращает первый элемент, но не удаляет его
        :return: первый элемент
        """
        assert not self.empty(), 'Queue is empty!'
        return self.m_front.item

    def __len__(self):
        return self.size
