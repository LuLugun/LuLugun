#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle
{
public:
    Rectangle();
    Rectangle(double, double);
    void setWidth(double);
    void setHeight(double);
    double getWidth()const; 
    double getHeight()const; 
    double getArea()const; 
    static int getNumOfRect();
private:
    double width;
    double height;
    static int numOfRect;
};
#endif