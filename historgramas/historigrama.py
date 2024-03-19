import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a local file
diabetes_df = pd.read_csv('pima-indians-diabetes.csv')

# Create a histogram of glucose levels
plt.hist(diabetes_df['Glucose'], bins=4, edgecolor='black')
plt.xlabel('Glucose Level')
plt.ylabel('Frequency')
plt.title('Distribution of Glucose Levels')
plt.xticks(range(0, 226, 25))
plt.show()









\begin{thebibliography}{12}
\bibitem{b1}Organización Mundial de la Salud. (2021). Diabetes. 
\bibitem{b2}Federación Internacional de Diabetes. (2019). Atlas de la Diabetes de la FID (9a edición).
\bibitem{b3}Han, J., Kamber, M., \& Pei, J. (2011). Data mining: concepts and techniques.
\bibitem{b4}Witten, I. H., Frank, E., \& Hall, M. A. (2011). Data Mining: Practical Machine Learning Tools and Techniques (3rd ed.).
\bibitem{b5}Hastie, T., Tibshirani, R., \& Friedman, J. (2009). The elements of statistical learning: data mining, inference, and prediction (2nd ed.).
\bibitem{b6} Fayyad, U., Piatetsky-Shapiro, G., \& Smyth, P. (1996). From data mining to knowledge discovery in databases. AI magazine, 17(3), 37-54.
\bibitem{b7}  Provost, F., \& Fawcett, T. (2013). Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking.
\bibitem{b8}Quinlan, J. R. (1986). Induction of decision trees. Machine learning, 1(1), 81-106.
\bibitem{b9} Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.
\bibitem{b10} Goodfellow, I., Bengio, Y., \& Courville, A. (2016). Deep Learning. MIT Press.
\bibitem{b11}``Google Research', ¿Qué es Colaboratory?
\bibitem{b12} ``El tutorial de Python'', Python Documentation. 
\end{thebibliography}
\end{document}



\begin{resumen}
 \textbf{\textit{Resumen}---Este artículo emplea la minería de datos para descubrir patrones relacionados con la incidencia de diabetes en mujeres. Se exploran diversos factores como el número de embarazos, niveles de glucosa, presión sanguínea, grosor de la piel, niveles de insulina, índice de masa corporal y edad. El objetivo es entender mejor la conexión entre estos factores y la diabetes en mujeres. El estudio se enfoca en implementar las distintas fases del proceso Knowledge Discovery in Databases (KDD), que abarca desde la selección de los datos hasta su procesamiento y transformación, seguido por un análisis para evaluar y presentar los resultados obtenidos.}\newline
 
\end{resumen}