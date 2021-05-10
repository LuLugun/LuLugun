#ifndef SCORE_H
#define SCORE_H
class BMI
{
public:
	BMI();
	BMI(double, double);
	double getBMI();
private:
	double weight;
	double height;
};
#endif

