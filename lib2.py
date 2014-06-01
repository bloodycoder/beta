# -*- coding: cp936 -*-
import pygame
from pygame.locals import *
class Button(object):
#�������һ����ť������������Ⱦ���ж��Ƿ񱻰��ϵĹ���
    def __init__(self, image_filename, position):

        self.position = position
        self.image = pygame.image.load(image_filename)

    def render(self, surface):
        # �ҳ��㷹�Ĵ�����,positionΪ���ĵ�����
        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2
        surface.blit(self.image, (x, y))

    def is_over(self, point):
        # ���point������Χ�ڣ�����True
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2

        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        return in_x and in_y
