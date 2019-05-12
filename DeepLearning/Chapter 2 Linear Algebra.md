# 1.Scalars,Vectors,Matrices and Tensors
## Scalars
We write scalars in italics ( e.g. \\(a,b,c\\)).

## Vectors
Typically we give vectors lower case names written in bold typeface, such as \\(\boldsymbol{x}\\). The elements of an \\(n\\) elements vector \\(\boldsymbol{x}\\) are \\(x_1,\cdots,x_n\\).
$$
\boldsymbol{x}=\begin{bmatrix} x_1\\\\x_2\\\\ \cdots \\\\x_n\end{bmatrix}
$$

## Matrices
We usually give matrices in upper-case variable names with bold typeface, such as \\(\boldsymbol{A}\\).
\\(\boldsymbol{A}_{i,:}\\) denotes the \\(i\\)-th row of \\(\boldsymbol{A}\\).
\\(\boldsymbol{A}_{:.i}\\) denotes the \\(i\\)-th column of \\(\boldsymbol{A}\\).

## Tensors
We denote a tensor named "A" with \\(\boldsymbol{\rm{A}}\\). 

# 2.Mulatiplying Matrices and Vectors
## matrix product 
The matrix product of matrices \\(\boldsymbol{A}\\) and \\(\boldsymbol{B}\\) is a thrid matrix \\(\boldsymbol{C}\\).
If \\(\boldsymbol{A}\\) is of shape \\(m\times n\\) amd  \\(\boldsymbol{B}\\) is of shape \\(n\times p\\), then \\(\boldsymbol{c}\\) is of shape \\(m\times p\\).

## element-wise product or Hadamard product
The hadamard product is a binary operation that takes two matrices of the same dimesions, and produces another matrix where each element \\(i,j\\) is the product of elements \\(i,j\\) of two origin matrices.

## dot product
The dot product between two vectors \\(\boldsymbol{x}\\) and \\(\boldsymbol{y}\\) of the same dimensionality is the matrix product \\(\boldsymbol{x^Ty}\\). We can think of the matrix product \\(\boldsymbol{C=AB}\\) as computing \\(C_{i,j}\\) as the dot product between row \\(i\\) of \\(\boldsymbol{A}\\) and column \\(j\\) of \\(\boldsymbol{B}\\)

## note
matrix multiplication is not commutative(\\(\boldsymbol{AB}=\boldsymbol{BA}\\) does not always hold), the dot product between two vectors is commutative: \\(\boldsymbol{x}^\rm{T}\boldsymbol{y}=\boldsymbol{y}^\rm{T}\boldsymbol{x}\\), since the dot product is a scalar.

# 3.Identity and Inverse Matrices

# 4.Linear Dependence and Span
# 5.Norms
# 6.Special Kinds of Matrices and Vectors
# 7.Eigendecomposition
# 8.Singular Value Decomposition(SVD)
# 9.The Moore-Penrose Pseudoinverse
# 10.The Trace Operator
# 11.The Determinant 
# 12.Example: Principal Components Analysis(PCA)