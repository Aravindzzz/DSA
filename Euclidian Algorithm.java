class Solution {
    /*
     * The Euclidean algorithm for computing the Greatest Common Divisor (GCD) recursively works as follows:
     *
     * Understanding the GCD Algorithm:
     * The Euclidean algorithm is based on the principle that:
     *
     * GCD(a, b) = GCD(b, a % b)
     * where % represents the modulus operator (remainder).
     *
     * Here's how the algorithm proceeds:
     *
     * Base Case: If b is 0, then the GCD is a. This is because when the remainder b reaches 0, the divisor a is the GCD.
     * Recursive Case: If b is not 0, the algorithm calls itself with b and a % b.
     */
    static long gcd(long a, long b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);  // Recursive call
    }

    public static void main(String[] args) {
        // Example usage
        long a = 48;
        long b = 18;
        System.out.println("GCD of " + a + " and " + b + " is: " + gcd(a, b));
    }
}
//LCM = A*B/GCD(A,B)


