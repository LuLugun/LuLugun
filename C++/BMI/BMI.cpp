#include "BMI.h"
BMI::BMI()
{
}
BMI::BMI(double newweight, double newheigh)
{
	weight = newweight;
	height = newheigh;
}
double BMI::getBMI()
{
	return weight / (height * height);
}