#!/usr/bin/env python3


class Hase:
    name = "Hase"  # global static
    __height = 10  # 'private' static members start with __

    def __init__(self, ears, legs) -> None:
        """ constructor """
        self.ears = ears   # public members
        self._legs = legs  # 'private' members start with __

    def __repr__(self) -> str:
        return f"I'm {Hase.name} with {self.ears} ears and {self._legs} legs"

    @property
    def legs(self):
        """ getter """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """ setter """
        self.__legs = legs


hase = Hase(4, 5)
hase.legs = 6

print(hase)
