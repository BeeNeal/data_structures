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
        self.prisonDays = dict()
        self.prisonDays[0] = self.cells
        # self.pattern = dict()

    # def findPattern(self, d):
    #     """Find the cycle, store cell day as key. SCRIPT"""

    #     tupled_day = tuple(self.cells)
    #     if tupled_day in self.pattern:
    #         print("PATTERN REPEATS AT DAY = {}".format(self.pattern[tupled_day]))
    #         return "PATTERN REPEATS AT DAY = {}".format(self.pattern[tupled_day])
    #     self.pattern[tupled_day] = d

    def showDays(self, days):
        """Store prison day pattern with day as key."""

        if days > 14:
            days = days % 14
        return self.prisonDays[days]
        # if day == 0:
        #     day = 14
        # repeats after 14


    def prisonAfterNDays(self, days):
        """Populate a dictionary with patterns of days - 14 b/c 8 cells """

        for d in range(1, 14):
            self.fill_prison(self.cells)
            self.prisonDays[d] = self.cells
        print(self.prisonDays)

            # self.findPattern(d) 

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
print(new_prison.prisonAfterNDays(7))

# above solution works great until there are billions of days... 
# takes several minutes to run 1000000000
# there must be a pattern, where the cycle repeats. 
# Use hashmap to find pattern -> store each iteration and access through keys

# lessons learned:
# OOP to re-use cells, passing into function call
# run a function call multiple times with range
# formatting long conditional statements to adhere to pep8 with () and whitespace

