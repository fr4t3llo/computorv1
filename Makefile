NAME = equ

CPPFLAGS = -Wall -Wextra -Werror 

SRC = src/main.cpp 

INC = includes/computorv1.hpp

OBJS = $(SRC:.cpp=.o)

all : $(NAME)

$(NAME) : $(OBJS)
	c++ $(CPPFLAGS) $^ -o $(NAME)

%.o : %.cpp $(INC)
	c++ $(CPPFLAGS) -c $< -o $@

clean :
	rm -f $(OBJS)

fclean : clean
	rm -f $(NAME)

# re : fclean $(NAME)
# CC = g++
# CFLAGS = -Wall -Wextra -Werror -std=c++11
# NAME = computor
# SRCDIR = .
# OBJDIR = obj
# SOURCES = main.cpp
# OBJECTS = $(SOURCES:%.cpp=$(OBJDIR)/%.o)

# all: $(NAME)

# $(NAME): $(OBJECTS)
# 	$(CC) $(OBJECTS) -o $(NAME)

# $(OBJDIR)/%.o: $(SRCDIR)/%.cpp
# 	@mkdir -p $(OBJDIR)
# 	$(CC) $(CFLAGS) -c $< -o $@

# clean:
# 	rm -rf $(OBJDIR)

# fclean: clean
# 	rm -f $(NAME)

# re: fclean all

# test: $(NAME)
# 	@echo "Testing basic cases..."
# 	@echo "\n=== Test 1: Quadratic with positive discriminant ==="
# 	./$(NAME) "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# 	@echo "\n=== Test 2: Linear equation ==="
# 	./$(NAME) "5 * X^0 + 4 * X^1 = 4 * X^0"
# 	@echo "\n=== Test 3: Degree > 2 ==="
# 	./$(NAME) "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# 	@echo "\n=== Test 4: Identity (any solution) ==="
# 	./$(NAME) "6 * X^0 = 6 * X^0"
# 	@echo "\n=== Test 5: No solution ==="
# 	./$(NAME) "10 * X^0 = 15 * X^0"
# 	@echo "\n=== Test 6: Negative discriminant ==="
# 	./$(NAME) "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"

# .PHONY: all clean fclean re test