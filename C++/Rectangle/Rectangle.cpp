#include "Rectangle.h"

int Rectangle::numOfRect = 0;

Rectangle::Rectangle()
{
    numOfRect++;
}
Rectangle::Rectangle(double newhight, double newwidth)
{
    height = newhight;
    width = newwidth;
    numOfRect++;
}
void Rectangle::setHeight(double newhight)
{
    height = newhight;
}
void Rectangle::setWidth(double newwidth)
{
    width = newwidth;
}
double Rectangle::getHeight() const
{
    return height;
}
double Rectangle::getWidth() const
{
    return width;
}
double Rectangle::getArea() const
{
    return height * width;
}
int Rectangle::getNumOfRect()
{
    return numOfRect;
}
