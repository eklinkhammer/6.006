from AuxHashFunctions import *
import pickle

class HashFunctions:
    def __init__(self, hash_functions):
        
        # Auxiliary hash functions
        self.aux_h1 = hash_functions.hash_1
        self.aux_h2 = hash_functions.hash_2
        
    def linear_probing_hash(self, key, i, m):
        # Use auxiliary hash function self.h1(k) to
        # implement linear probing - a hash function of the form h(k, i) in range [0 ... m-1]
        # See CLRS pp272 for details
        
		#
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##
        
    def double_hashing_hash(self, key, i, m):
        # Use auxiliary hash functions self.h1(k) and self.h2(k)
        # to implement double hashing - a hash function of the form h(k, i) in range [0 ... m-1]
        # See CLRS pp272-274 for details
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##

class OpenAddressedDictionary:
    def __init__(self, array, hash_function):
        # use self.array to store your key-value pairs. The array is pre-allocated, and has capacity m.
        # Initially, all elements of self.array are set to (None, None)
        # 
        self.array = array;
        
        # the fixed, static capacity of self.array is exactly m
        self.m = len(array)
        
        # this hash function h(k, i, m) can be used to map a key k to an index in range [0 .. m-1]
        self.hash_function = hash_function;

    def insert(self, key, value):
        # insert
        # - associate a key ("key") with a value ("value")
        #   in a dictionary ("self.array"), provided the key 
        #   is not already in the dictionary, and return True.
        #   If the key is in the dictionary already, return False, and
        #   do not modify the dictionary. Also return False if the dictionary is full.
        #
        # Return Value:
        # - True if "insert" succeeds (i.e. key not already mapped, dictionary not full)
        # - False otherwise (i.e. key already mapped to a value, or dictionary is full).
        #  Do not modify the dictionary in if insertion fails!
        #
        # TODO: Use open addressing (the hhash_function provided specifies the exact strategy among linear probing and double hashing)
        # to implement insert. Feel free to create helper methods.
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##

    def delete(self, key):
        # delete
        # - remove from the dictionary ("self.array" the key-value mapping
        #   given by a key ("key"), provided the mapping exists.
        #
        # Return Value:
        # - True if "delete" succeeds (key was present in the dictionary)
        # - False otherwise (key was not present in the dictionary)
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##

    def search(self, key):
        # search
        # - find and return the value associated with "key" in the dictionary (self.array).
        #   Return None if the key is not in the dictionary.
        #
        # Return Value:
        # - the value associated with "key" if the key is in the dictionary.
        # - None if the key is not in the dictionary.
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##
		
class CuckooDictionary:
    def __init__(self, array, aux_hash_functions):
        # use self.array to store your key-value pairs. The array is pre-allocated, and has capacity m.
        # Initially, all elements of self.array are set to (None, None)
        # 
        self.array = array;
        
        # the fixed, static capacity of self.array is exactly m
        self.m = len(array)
        
        # self.h1 and self.h2 are two hash functions h(k, m) that map a key to an index in range [0 .. m-1]
        self.aux_hash_functions = aux_hash_functions
        self.h1 = aux_hash_functions.hash_1
        self.h2 = aux_hash_functions.hash_2
        
        # This is used to limit. You should not need to use this variable in your code.
        self.max_evicts = 10
    
    def insert(self, key, value):
        # insert
        # - associate a key ("key") with a value ("value")
        #   in a dictionary ("self.array"), provided the key 
        #   is not already in the dictionary, and return True.
        #   If the key is in the dictionary already, return False, and
        #   do not modify the dictionary. Also return False if the dictionary is full.
        #
        # Return Value:
        # - True if "insert" succeeds (i.e. key not already mapped, dictionary not full)
        # - False otherwise (i.e. key already mapped to a value, or dictionary is full).
        #  Do not modify the dictionary in if insertion fails!
        #
        # TODO: Use cuckoo hashing to implement insert. Feel free to create helper methods.
        
        if (self.search(key) is not None):
            return False
        else:
            for e in range(0, self.max_evicts):
                #
				# BEGIN YOUR CODE 
				#
				
				raise NotImplementedError
				
				##
				## END STUDENT CODE
				##
                    
        # At this point, we've performed O(self.max_evicts evictions), and failed to complete the insertion.
        # We would normally rehash with new hash functions. You are not responsible for this in your Pset 3
        # because we designed our test cases to not require rehashing by keeping the load factor small.
        # If you design your own test cases, you may see failed insertions due to eviction loops.
        # This is to be expected, since, again you aren't responsible for rehash()
        
        #if not self.rehash(key, value):
        #    return False
        
        # re-insert the last evicted item (on next iteration).
        # The (key, value) pair is exactly the last evicted item that is currently not in the dictionary
        
        # Looks like we've failed to insert into the hash.
        # The reason is a high loading factor (the dictionary is more or less full), up to hash function quality.
        # It is appropriate to give up in this case
        #return True
        
        raise Exception("failed to insert a key into a Cuckoo dictionary. Our test cases are designed not to do this if you use h1 and h2 correctly.")
    
    def delete(self, key):
        # delete
        # - remove from the dictionary ("self.array" the key-value mapping
        #   given by a key ("key"), provided the mapping exists.
        #
        # Return Value:
        # - True if "delete" succeeds (key was present in the dictionary)
        # - False otherwise (key was not present in the dictionary)
        
        #raise NotImplementedError()
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##

    def search(self, key):
        # search
        # - find and return the value associated with "key" in the dictionary (self.array).
        #   Return None if the key is not in the dictionary.
        #
        # Return Value:
        # - the value associated with "key" if the key is in the dictionary.
        # - None if the key is not in the dictionary.
        
        #raise NotImplementedError()
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##
    
    def rehash(self, last_key, last_value):
        # enumarate all items in the array, and add the last-evicted key-value pair
        items = []
        for (key, value) in self.array:
            if key is not None:
                items.append((key, value))
        items.append((last_key, last_value))
        
        # clear the array!
        for i in range (0, self.m):
            self.array[i] = (None, None)
        
        # mutate to new hash functions
        self.aux_hash_functions.change_hash_functions()
        
        # re-insert all elements
        for (key, value) in items:
            self.insert(key, value)
        
        return True

# You may find this helpful when averaging ratings of multiple films
def mean(L):
    s = float(sum(L))
    l = len(L)
    
    if l != 0:
        return s/l
    else:
        raise Exception("mean of zero numbers is not defined! You tried to take a mean of an empty list.")

class IMDB:
    #
    # Arguments:
    # array_large - a pre-allocated array of 30000 elements (initially all (None, None) )
    # array_small - a pre-allocated array of 10000 elements (initially all (None, None) )
    #
    def __init__(self, array_large, array_small, linear_probing_hash, double_hashing_hash):
        
        # self.films_list is a list of film entries, where
        # each film entry is of the form [film, rating, year, [actors]], where
        #    film is a string film movie "Godfather"
        #    rating is a number (float)
        #    year is an integer
        #    [actors] is a list of strings of actors' names such as "Matt Daemon"
        #
        # There approximately 20000 film entries in self.actors_list.
        self.films_list = pickle.load(open('films_list.pickle', 'rb'))
        print ("There are " + str(len(self.films_list)) + " film entries")
        
        # self.actors_list is a list of actor entries, where
        # each actor entry is of the form [name, [films]], where
        #    name is a string name of the actor, such as "Matt Daemon"
        #    [films] is a list of string film titles such as ["Godfather", "Quantum of Solace", "Oldboy"]
        #
        # There approximately 8000 actor entries in self.actors_list.
        self.actors_list = pickle.load(open('actors_list.pickle', 'rb'))
        print ("There are " + str(len(self.actors_list)) + " actor entries")
        
        # Initialize the data structure you will use to implement career_impact queris below.
        # Use the two arrays as storage with caution - 20,000 films cannot fit in array_small
        
        #
        # BEGIN YOUR CODE 
        #
        
        raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##
    
    def career_impact(self, film, actor):
        # return a career impact metric for a given actor and a given film, as specified in the problem set  PDF
        
        #
        # BEGIN YOUR CODE 
        #
        
		raise NotImplementedError
		
		##
        ## END STUDENT CODE
        ##
		
