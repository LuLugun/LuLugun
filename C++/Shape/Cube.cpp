#include "Cube.h"

Cube::Cube(double length)
{
    setLength(length);
}
Cube::Cube(double length, const string& color, bool filled)
{
    setLength(length);
    setColor(color);
    setFilled(filled);
}
void Cube::setLength(double new1)
{
    length = new1;
}
double Cube::getLength()const
{
    return length;
}
double Cube::getVolume()const
{
    return length * length * length;
}
double Cube::getArea()const
{
    return 6.0 * length * length;
}
string Cube::toString()const
{
    return "Cube";
}