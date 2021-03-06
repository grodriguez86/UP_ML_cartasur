# ####################################################################
#
#  LIBRARY
#    normalizer
#
#  DESCRIPTION
#    The aim of this library is to have normalizer helper functions to
#  apply to the datasets. So since it's often to have to normalize and
#  translate data from one value to another, we have created a library
#  here that does that for us in a simple manner.
#
#    The library assumes that the input is a dataframe (df) which is
#  the objects generated by the Pandas library.
#
# --------------------------------------------------------------------



#  normalize_string
#    df : [Pandas dataFrame]
#    column : [String] name of the column you want to normalize
#    mapping : [Python associatve array]
#
#  This function converts all the columns on a given dataframe from
#  a string to some value specified in a mapping.
#  The big difference between the previous version of this, is that
#  the user MUST know what is the mapping beforehand.
#  This is particularly useful when you WANT to know how the string
#  values were replaced by numbers.
# --------------------------------------------------------------------
def normalize_string_mapping(df, column, mapping):
    df[column].replace(mapping, inplace=True)


#  normalize_amount
#    df : [Pandas dataFrame]
#    column : [String] name of the column you want to normalize
#    round_to : [integer number]
#
#  This function remove "in between" numbers in a "floor" manner.
#  So for example if you have the numbers [5, 10, 12, 20, 24] and you
#  round to 10, then your set will end up being [5, 10, 10, 20, 20]
#  because all the numbers inbetween will be "floored" to the lower
#  number that is divided by 10.
# --------------------------------------------------------------------
def normalize_amount(df, column, round_to=2500):
    df[column] = df[column].apply(lambda x: int(x)-(int(x) % round_to))
