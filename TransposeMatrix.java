public class TransposeMatrix {

    static final int N = 8;

    //Stores transpose of A[][] in B[][]
    public static void transpose(int A[][], int B[][]) {
        int i, j;

        for(i = 0; i < N; i++) {
            for(j = 0; j < N; j++) {
            	B[i][j] = A[j][i];            	
            }
        }
    }

    public static void main(String[] args) {
        int A[][] = {{ 0,  3,  4,  5, 58, 59, 60, 63 },
	        		{  1,  2,  7,  6, 57, 56, 61, 62 },
	        		{ 14, 13,  8,  9, 54, 55, 50, 49 },
	        		{ 15, 12, 11, 10, 53, 52, 51, 48 },
	        		{ 16, 17, 30, 31, 32, 33, 46, 47 },
	        		{ 19, 18, 29, 28, 35, 34, 45, 44 },
	        		{ 20, 23, 24, 27, 36, 39, 40, 43 },
	        		{ 21, 22, 25, 26, 37, 38, 41, 42 },
                       };

        int B[][] = new int[N][N], i, j;

        transpose(A, B);
        System.out.println("Result matrix is ");
        for(i = 0; i < N; i++) {
            for(j = 0; j < N; j++) {
                System.out.print(B[i][j] + " ");
            }
            System.out.println();
        }
    }
}