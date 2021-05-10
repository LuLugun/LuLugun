#ifndef SHAPE_H
#define SHAPE_H
#include <string>
using namespace std;
class Shape
{
protected:
    Shape();
    Shape(const string& color, bool filled);
public:
    string toString()const;
    void setColor(const string& color);
    string getColor()const;
    void setFilled(bool filled);
    bool isFilled()const;
    virtual double getArea()const = 0;
private:
    string color;
    bool filled;
};
#endif