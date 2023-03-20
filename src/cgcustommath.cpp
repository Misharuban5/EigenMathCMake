#include "cgcustommath.hpp"

Eigen::Array22f matrix(int a, int b) {
    return Eigen::Matrix<float, 2, 2>::Identity() * a + Eigen::Matrix<float, 2, 2>::Constant(1)*b;
}