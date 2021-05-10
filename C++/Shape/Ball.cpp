#include "Ball.h"

Ball::Ball(double radius)
{
    setRadius(radius);
}
Ball::Ball(double radius, const string& color, bool filled)
{
    setRadius(radius);
    setColor(color);
    setFilled(filled);
}
void Ball::setRadius(double new1)
{
    radius = new1;
}
double Ball::getRadius()const
{
    return radius;
}
double Ball::getVolume()const
{
    return 4.0 / 3.0 * 3.14159 * radius * radius * radius;
}
double Ball::getArea()const
{
    return 4.0 * 3.14159 * radius * radius;
}
string Ball::toString()const
{
    return "Ball";
}