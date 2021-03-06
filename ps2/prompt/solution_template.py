import argparse
import pickle
import copy

class Heap:

    def __init__(self, sorting_key):
        """Initializes a new instance of a heap.

        Args:
            sorting_key: Specifies the attribute of the object inserted
            into the heap, on the basis of which the heap was created.
        """
        self.heap = list()
        self.mapping = dict()
        self.sorting_key = sorting_key
    ##########################################################################
    # STANDARD HEAP OPERATIONS
    ##########################################################################

    def heapify_up(self, child):
        """Standard heapify operation, as described in CLRS.
        Works by swapping the element originially at index child in the heap
        with its parent until the heap property is satisfied. Modifies the
        appropriate heap attribute

        Args:
            child: Index of the element that violates the heap property

        Returns:
            None
        """
        parent = (child - 1) / 2
        # Swaps the element originally at the index child with its parent
        # until the value of the specifed attribute of the parent is greater
        # than the value of the specified attribute of the element itself
        while (getattr(self.heap[parent], self.sorting_key) <
               getattr(self.heap[child], self.sorting_key)):
            if (parent == -1):
                # This means child was 0, which means we have reached the
                # top of the heap
                return

            # Swap the mappings as well to ensure that future references in
            # the mapping dict refer to the correct position of the object in
            # the heap
            self.mapping[self.heap[parent].player] = child
            self.mapping[self.heap[child].player] = parent

            # Swap the parent and the child
            temp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = temp

            # Move the child and parent pointers up the heap
            child = parent
            parent = (child - 1) / 2

    def heapify_down(self, parent):
        """Same as heapify_up, but moves an element down instead of up.

        Args:
            parent: Index of the element that violates the heap property

        Returns:
            None
        """
        left_child = parent * 2 + 1
        right_child = parent * 2 + 2
        if ( left_child >= len( self.heap ) ):
            left_child = parent
        if ( right_child >= len( self.heap ) ):
            right_child = parent

        #Heap Property is violated whenever Parent is less than one of its children
        #Swap the parent with the greater child, continue down until it is bigger
        # than both of its children
        while( getattr( self.heap[parent], self.sorting_key ) < max( getattr( self.heap[left_child], self.sorting_key ), getattr( self.heap[right_child], self.sorting_key ) ) ): # Change to || if needed
            if ( getattr( self.heap[right_child], self.sorting_key )  > getattr( self.heap[left_child], self.sorting_key) ):
                temp = self.heap[right_child]
                temp_index = right_child
            else:
                temp = self.heap[left_child]
                temp_index = left_child
            
            #Swaps the mappings
            self.mapping[self.heap[parent].player] = temp_index
            self.mapping[self.heap[temp_index].player] = parent

            #Swap the parent and the max child
            self.heap[temp_index] = self.heap[parent]
            self.heap[parent] = temp

            #print self.heap
            parent = temp_index
            left_child = parent * 2 + 1
            right_child = parent * 2 + 2
            #print parent
            #print left_child
           # print right_child
            #print "\n"
            if ( left_child >= len( self.heap ) ):
                left_child = parent
            if ( right_child >= len( self.heap ) ):
                right_child = parent
    def extract_max(self):
        """Returns the maximum element in the specified heap

        Returns:
            An object from the heap with maximum value of self.sorting_key
        """
        #print self.heap
        
        max_element = self.heap[0]
        #print self.heap
        #print len(self.heap)
        if ( len(self.heap) == 1 ):
            self.heap = []
            return max_element
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_element

    def insert(self, element):
        """Inserts element into the specified heap. Modifies the internal heap
        data structure

        Args:
            element: PlayerRecord object that needs to be inserted into the
            heap

        Returns:
            None
        """

        # Append the new element to the end of the heap, and then
        # move the element up the heap as necessary
        self.heap.append(element)
        child = len(self.heap) - 1
        self.mapping[element.player] = child
        self.heapify_up(child)

    def get_index(self, element):
        """Returns the index of the provided element in the heap

        Args:
            element: The element whose index needs to be returned

        Returns:
            Index of the element in the heap if the element is in the heap
            None, otherwise
        """
        return self.mapping.get(element.player, None)

    def validate_heap(self):
        """Validates that the heap specified by heap_name satisfies the heap
        property at every node

        Returns:
            True if heap property is satisfied at every node of the heap,
            False otherwise
        """
        heap = [getattr(ele, self.sorting_key) for ele in self.heap]
        remaining_elements = [0]
        n = len(heap)
        while (len(remaining_elements) != 0):
            parent = remaining_elements.pop()
            child1 = (2 * parent) + 1
            child2 = (2 * parent) + 2
            if (child1 < n):
                remaining_elements.append(child1)
                if (heap[child1] > heap[parent]):
                    return False
            if (child2 < n):
                remaining_elements.append(child2)
                if (heap[child2] > heap[parent]):
                    return False
        return True


# Statistics for a particular player are encapsulated by a PlayerRecord
class PlayerRecord:

    """Encapsulates statistics of a player

    Attributes:
        player: Name of the player
        ab: Number of at-bats by the player
        hits: Number of 'hits' by the player
        avg: Average number of hits = hits / ab
        rbi: Number of 'runs-batted-in' by the player
    """

    def __init__(self, player, ab, hits, rbi):
        """Initializes a new instance of PlayerRecord, setting the
        various statistic values as provided

        Args:
            player: Name of the player
            ab: Number of at-bats by the player
            hits: Number of hits by the player
            rbi: Number of rbis by the player
        """
        self.player = player

        self.ab = ab
        self.hits = hits
        if ab == 0:
            self.avg = 0.0
        else:
            self.avg = float(hits) / float(ab)
        self.rbi = rbi

    def __repr__(self):
        return '%s--Ab:%d, Hits:%d, Avg:%.3f, Rbi:%d' % (
            self.player, self.ab, self.hits, self.avg, self.rbi)


class Problem:

    """Represents an instance of a problem. Implements operations required in
    the problem statement

    Attributes:
        player_record_mapping: Mapping between player name and PlayerRecord
        object corresponding to the player
    """

    def __init__(self):
        self.player_record_mapping = dict()
        # Idea: Have a 4 heaps running, each for a different statistic
        self.players_ab = Heap("ab")
        self.players_rbi = Heap("rbi")
        self.players_avg = Heap("avg")
        self.players_hits = Heap("hits")
        # TODO: Initialize your data structures here

    ###########################################################################
    # OPERATIONS SPECIFIED IN PROBLEM STATEMENT
    ###########################################################################

    def new_at_bat(self, player, hits, rbi):
        """Represents the new_at_bat operation. Checks if the given player
        has been seen before, if so just updates the corresponding PlayerRecord
        object (and corresponding heaps as well); otherwise creates a new
        object of the PlayerRecord class corresponding to the new player
        and adds this new object to all required heaps

        Args:
            player: Name of the player whose record needs to created / updated
            hits: Number of hits
            rbi: Number of runs-batted-in

        Returns:
            None
        """
        if player in self.player_record_mapping:
            record = self.player_record_mapping[player]
            record.ab = record.ab + 1
            record.hits = record.hits + hits
            record.rbi = record.rbi + rbi
            if record.ab == 0:
                pass
            else:
                record.avg = float(record.hits) / float(record.ab)
            # If those changed any rankings, update
           # if ( not self.players_ab.validate_heap() ):
           
            index = self.players_ab.get_index(record)
            self.players_ab.heapify_up(index)
            self.players_ab.heapify_down(index)
           # if ( not self.players_rbi.validate_heap() ):
            index = self.players_rbi.get_index(record)
            self.players_rbi.heapify_up(index)
            self.players_rbi.heapify_down(index)
           # if ( not self.players_hits.validate_heap() ):
            index = self.players_hits.get_index(record)
            self.players_hits.heapify_up(index)
            self.players_hits.heapify_down(index)
           # if ( not self.players_avg.validate_heap() ):
            index = self.players_avg.get_index(record)
            self.players_avg.heapify_up(index)
            self.players_avg.heapify_down(index)

        else:
            record = PlayerRecord(player,1,hits,rbi)
            self.players_ab.insert(record)
            self.players_rbi.insert(record)
            self.players_hits.insert(record)
            self.players_avg.insert(record)
            self.player_record_mapping[player] = record
    def current_stats(self, player):
        """Represents the current_stats operation.

        Args:
            player: Name of the player

        Returns:
            PlayerRecord instance that encapsulates statistics of the
            specified player if the player name exists in the database.
            PlayerRecord(None, 1, 0, 0) if the player name does not exist
            in the database.
        """
        if player in self.player_record_mapping:
            return self.player_record_mapping[player]
        else:
            return PlayerRecord(None, 1, 0, 0)

    def current_best(self, stat, k):
        """Represents the current_best operation.

        Args:
            stat: The type of statistic for which we need to return
            the top k players
            k: The number of players to return
        Returns:
            If k <= n, a list of k PlayerRecord objects in decreasing order of
            the given statistic
            If k > n, a list of n PlayerRecord objects in decreasing order of
            the given statistic
        """
        index = 0
        top_k = [] 
        if ( stat == "rbi" ):
            heap = self.players_rbi
        if ( stat == "ab" ):
            heap = self.players_ab
        if ( stat == "hits" ):
            heap = self.players_hits
        if ( stat == "avg" ):
            heap = self.players_avg
        #x = copy.deepcopy(heap)
        n = len(heap.heap)
        while( index < k and index < n ):
           top_k.append( heap.extract_max())
           index += 1
        for x in top_k:
            heap.insert(x)
        return top_k    

###############################################################################
# DO NOT CHANGE THE CODE BELOW
###############################################################################


def run(filename, debug=False):
    """Runs the code specified in the Program class against the provided
    test driver file.

    Args:
        filename: File path of the test driver file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        return run_from_list(lines, debug)
    return None


def run_from_list(line_list, debug=False):
    """Runs the code specified in the Program class against the provided
    line_list

    Args:
        line_list: List of input lines

    Returns:
        List of results
    """
    problem = Problem()
    results = list()
    for line in line_list:
        line = line.strip()
        tokens = line.split('\t')
        operation_type = tokens[0]
        # Following operations allowed:
        # 1. n -- new_at_bat(player, hits, rbi)
        # 2. cs -- current_stats(player)
        # 3. cb -- current_best(heap_name, k)
        if (operation_type == 'n'):
            player = tokens[1]
            hits = int(tokens[2])
            rbi = int(tokens[3])
            problem.new_at_bat(player, hits, rbi)
        elif (operation_type == 'cs'):
            player = tokens[1]
            cs = problem.current_stats(player)
            results.append(
                ('cs', (cs.player, cs. ab, cs.hits, cs.avg, cs.rbi)))
            if debug:
                print cs
        elif (operation_type == 'cb'):
            heap_name = tokens[1]
            k = int(tokens[2])
            cb = problem.current_best(heap_name, k)
            transformed_cb = [
                (stat.player, stat.ab, stat.hits, stat.avg, stat.rbi)
                for stat in cb]
            results.append((('cb', heap_name), transformed_cb))
            if debug:
                print cb
    return results


def process_results(results):
    MAPPING = {'player': 0, 'ab': 1, 'hits': 2, 'avg': 3, 'rbi': 4}
    processed_results = list()
    for result in results:
        (result_type, val) = result
        if result_type == 'cs':
            processed_results.append(val)
        else:
            (_, heap_name) = result_type
            processed_list = [element[MAPPING[heap_name]] for element in val]
            processed_results.append(processed_list)
    return processed_results


if __name__ == '__main__':
    import cProfile
    parser = argparse.ArgumentParser(description='Program arguments')
    parser.add_argument('--c', action='store_true')
    parser.add_argument('input_file')
    args = parser.parse_args()
    input_lines, gold_processed_results, _ = pickle.load(open(args.input_file))
    if args.c:
        results = run_from_list(input_lines)
        processed_results = process_results(results)
        if processed_results != gold_processed_results:
            print "TEST FAILED"
        else:
            print "TEST PASSED"
    else:
        cProfile.run("run_from_list(input_lines)")
