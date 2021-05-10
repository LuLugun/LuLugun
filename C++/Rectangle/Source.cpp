#include <iostream>
#include "Rectangle.h"
#include<iomanip>
using namespace std;

int main()
{
	double h1, w1, h2, w2, h3, w3;
	cin >> h1 >> w1 >> h2 >> w2 >> h3 >> w3;
	Rectangle r1(h1, w1);
	Rectangle r2(h2, w2);
	Rectangle r3(h3, w3);
	cout << r1.getHeight() << " " << r1.getWidth() << " " << r1.getArea() << endl;
	cout << r2.getHeight() << " " << r2.getWidth() << " " << r2.getArea() << endl;
	cout << r3.getHeight() << " " << r3.getWidth() << " " << r3.getArea() << endl;
	cout << Rectangle::getNumOfRect() << " Rectangles" << endl;
	return 0;
}