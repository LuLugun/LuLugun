#ifndef SHAPE3D_H
#define SHAPE3D_H
#include "Shape.h"
#include <string>
using namespace std;
class Shape3D :public Shape
{
public:
    string toString()const;
    virtual double getVolume()const = 0;
};
#endif