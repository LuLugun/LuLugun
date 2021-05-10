#ifndef SHAPE2D_H
#define SHAPE2D_H
#include "Shape.h"
#include <string>
using namespace std;
class Shape2D :public Shape
{
public:
    string toString()const;
    virtual double getPerimeter()const = 0;
};
#endif