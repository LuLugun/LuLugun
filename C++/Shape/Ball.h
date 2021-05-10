#ifndef BALL_H
#define BALL_H
#include "Shape3D.h"

class Ball : public Shape3D
{
public:
    Ball();
    Ball(double);
    Ball(double radius, const string& color, bool filled);
    void setRadius(double);
    double getRadius()const;
    double getVolume()const;
    double getArea()const;
    string toString()const;
private:
    double radius;
};
#endif