#pragma once
#include <Eigen/Dense>

/**
 * This function should: 
 * - Create a 2x2 identity matrix. 
 * - Multiply the matrix by a. 
 * - Add b to the matrix. 
 * - Return the resulting matrix. 
*/
Eigen::Array22f matrix(int a, int b);