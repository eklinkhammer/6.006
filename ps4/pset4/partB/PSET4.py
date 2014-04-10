from decimal import Decimal
from math import log as log
import math
# Find the cube root of 7
def partA( val, guess ):
  x0 = guess
  i = 0
  while ( i < 10 ):
    xn = (1.0/3)* (val / (x0 * x0 ) + 2 * x0 )
    x0 = xn
    print(xn)
    i = i + 1
    
if (__name__ == "__main__" ):
  partA(7,2)

# Returns the next guess after one iteration of Newton's method.
#
# Arguments:
#  - number: The number whose cube root is to be calculated.
#  - guess: The current guess of the cube root.
def CubeRootNewtonIteration(number, guess):
  assert type(number) == int

  # BEGIN STUDENT CODE
  return (1 / 3.0 ) * ( number / ( guess * guess ) + 2 * guess )
  # END STUDENT CODE


# Returns an integer guess for the cube root of the number.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
def CubeRootGuess(number):
  assert type(number) == int

  # BEGIN STUDENT CODE
  # Completely lost here
  return int( math.pow( number, 1/3.0 ))
  # END STUDENT CODE


# Returns the best floating-point approximation to the cube root of the number.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
def FloatCubeRoot(number):
  assert type(number) == int

  # BEGIN STUDENT CODE
  target_precision = log(number, 2) + 4 # Breaks if 3 or lower
  current = 0
  guess = CubeRootGuess(number) * 1.0

  while ( current < target_precision ):
    current = current + 1
    guess = ( number / ( guess * guess) + 2 * guess ) / 3
  return guess
  # END STUDENT CODE


# Returns a guess of the reciprocal of the given decimal number.
#
# Arguments:
# - number: The decimal number whose reciprocal is to be guessed.
def ReciprocalGuess(number):
  assert type(number) == Decimal

  # BEGIN STUDENT CODE
  # From Kevin on Piazza
  x = number.shorten(1)
  longX = long(x.significand)
  return Decimal( long(1.0 / longX * 10), ( -1 * x.exponent) -1, number.precision)
  # END STUDENT CODE


# Returns the reciprocal of the give decimal number, computed to the same
# precision as number itself (i.e., number.precision).
#
# Arguments:
# - number: The decimal number whose reciprocal is to be computed.
def DecimalReciprocal(number):
  assert type(number) == Decimal

  # BEGIN STUDENT CODE
  guess = ReciprocalGuess(number)
  calculations_needed = log(number.precision, 2) + 1 # Breaks without 1 sometimes
  index = 0
  while( index < calculations_needed ):
    index = index + 1
    guess =  guess * ( 2 - number * guess )
  return guess
  # END STUDENT CODE

  
# Returns the best approximation to the cube root of the number using decimal
# numbers with the given number of digits of precision.
#
# Arguments:
# - number: The number whose cube root is to be calculated.
# - precision: The number of digits of precision to use.
def DecimalCubeRoot(number, precision):
  assert type(number) == int
  assert type(precision) == int

  # Note: You will need to pass reciprocal=DecimalReciprocal when creating
  #       Decimal numbers with support for division.
  
  # BEGIN STUDENT CODE
  fudge_factor = 3
  guess = CubeRootGuess(number)
  target_precision = log( precision, 2) + fudge_factor
  current = 0
  decimal_guess = Decimal(guess, precision=precision + 100, reciprocal=DecimalReciprocal)
  decimal_number = Decimal(number, precision=precision + 100, reciprocal=DecimalReciprocal)
  decimal_number_div = decimal_number / 3
  decimal_two_thirds = Decimal(2, precision=precision + 100, reciprocal=DecimalReciprocal)
  decimal_two_thirds /= 3
  while ( current < target_precision ):
    current += 1
    decimal_guess = decimal_number_div / ( decimal_guess * decimal_guess) + decimal_two_thirds * decimal_guess
  return decimal_guess.shorten(precision)
  # END STUDENT CODE
