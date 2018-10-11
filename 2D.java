
import java.io.*; 

public class Sort2DMatrix { 

	static int sortRowWise(int m[][]) 
	{ 
		
		for (int i = 0; i < m.length; i++) { 

			
			for (int j = 0; j < m[i].length; j++) { 

				
				for (int k = 0; k < m[i].length - j; k++) { 
					if (m[i][k] > m[i][k + 1]) { 

						
						int t = m[i][k]; 
						m[i][k] = m[i][k + 1]; 
						m[i][k + 1] = t; 
					} 
				} 
			} 
		} 

		
		for (int i = 0; i < m.length; i++) { 
			for (int j = 0; j < m[i].length; j++) 
				System.out.print(m[i][j] + " "); 
			System.out.println(); 
		} 

		return 0; 
	} 

	
	public static void main(String args[]) 
	{ 
		int m[][] = { { 6, 8, 7, 1 }, 
					{ 4, 3, 0, 2 }, 
					{ 9, 5, 4, 2 }, 
					{ 7, 3, 1, 2 } }; 
		sortRowWise(m); 
	} 
} 
