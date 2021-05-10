#include "Shape.h"

Shape::Shape()
{
    color = "white";
    filled = false;
}
Shape::Shape(const string& color, bool filled)
{
    setColor(color);
    setFilled(filled);
}
void Shape::setColor(const string& color)
{
    this->color = color;
}
string Shape::getColor()const
{
    return color;
}
void Shape::setFilled(bool filled)
{
    this->filled = filled;
}
bool Shape::isFilled()const
{
    return filled;
}
string Shape::toString()const
{
    return "Shape";
}