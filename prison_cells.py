# There are 8 prison cells in a row, and each cell is either occupied or vacant.

# Each day, whether the cell is occupied or vacant changes according to the 
# following rules:

# If a cell has two adjacent neighbors that are both occupied or both vacant, 
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the 
# row can't have two adjacent neighbors.)

# We describe the current state of the prison in the following way: 
# cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

# Given the initial state of the prison, return the state of the prison after 
# N days (and N such changes described above.)
class Prison:

    def __init__(self, cells):
        """use the init here, so can modify same prison object when repeatedly 
        calling same method
        """

        self.cells = cells

    def prisonAfterNDays(self, days):
        """ """

        self.prisonAfterDay = dict()

        for d in range(days):
            # print(self.cells)
            self.fill_prison(self.cells)
            self.prisonAfterDay[tuple(self.cells)] = d
        
        return self.cells

    def fill_prison(self, cells):
        """ """

        new_cells = [self.cells[0]]
        for i in range(1,7):
            if (
                self.cells[i-1] == 1 and self.cells[i+1] == 1 or
                self.cells[i-1] == 0 and self.cells[i+1] == 0
                ):
                new_cells.append(1)
            else:
                new_cells.append(0)
        new_cells.append(0)


        self.cells = new_cells

new_prison = Prison([0, 1, 0, 1, 1, 0, 0, 1])
print(new_prison.prisonAfterNDays(90))

# above solution works great until there are billions of days... 
# takes several minutes to run 1000000000
# there must be a pattern, where the cycle repeats. 
# Use hashmap to find pattern -> store the final

# lessons learned:
# OOP to re-use cells, passing into function call
# run a function call multiple times with range
# formatting long conditional statements to adhere to pep8 with () and whitespace
