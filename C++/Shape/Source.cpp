#include "Ball.h"
#include "Circle.h"
#include "Cube.h"
#include "Rectangle.h"
#include "Shape.h"
#include "Shape2D.h"
#include "Shape3D.h"
#include <iostream>
#include <iomanip>
using namespace std;

bool equalArea(const Shape& s1, const Shape& s2)
{
	return s1.getArea() == s2.getArea();
}
bool equalVolume(const Shape3D& s3D1, const Shape3D& s3D2)
{
	return s3D1.getVolume() == s3D2.getVolume();
}
bool equalPerimeter(const Shape2D& s2D1, const Shape2D& s2D2)
{
	return s2D1.getPerimeter() == s2D2.getPerimeter();
}
void display(const Shape& s)
{
	cout << s.getColor() << "," << fixed << setprecision(2) << s.getArea() << endl;
}

int main()
{
	Circle circle(5, "yellow", 1);
	Rectangle rectangle(3, 4, "red", 0);
	Ball ball(5, "blue", 1);
	Cube cube(4, "black", 0);
	cout << "circle," << fixed << setprecision(0) << circle.getRadius() << ",";
	display(circle);
	cout << "rectangle," << fixed << setprecision(0) << fixed << setprecision(0) << rectangle.getWidth() << "," << fixed << setprecision(0) << rectangle.getHeight() << ",";
	display(rectangle);
	cout << "ball," << fixed << setprecision(0) << ball.getRadius() << ",";
	display(ball);
	cout << "cube," << fixed << setprecision(0) << cube.getLength() << ",";
	display(cube);
	if (equalPerimeter(circle, rectangle))
	{
		cout << "circle " << circle.getPerimeter() << " == " << "rectangle " << rectangle.getPerimeter() << endl;
	}
	else
		cout << "circle " << circle.getPerimeter() << " != " << "rectangle " << rectangle.getPerimeter() << endl;
	if (equalVolume(ball, cube))
	{
		cout << "ball " << ball.getVolume() << " == " << "cube " << cube.getVolume() << endl;
	}
	else
		cout << "ball " << ball.getVolume() << " != " << "cube " << cube.getVolume() << endl;
	return 0;
}