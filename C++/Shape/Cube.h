#ifndef CUDE_H
#define CUDE_H
#include "Shape3D.h"

class Cube : public Shape3D
{
public:
    Cube();
    Cube(double);
    Cube(double length, const string& color, bool filled);
    void setLength(double);
    double getLength()const;
    double getVolume()const;
    double getArea()const;
    string toString()const;
private:
    double length;
};
#endif