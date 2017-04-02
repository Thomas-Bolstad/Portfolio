//Functions for the classes:

#include <vector>
#include <fstream>
#include <cstdlib>

// Start of Board class:

Board::Board(char filename[]) 
{
	//converts the string into a constant char object
	//since fstream wotn work with strings:
	
	
	//char file_char();
	//file_char = new char [filename.size()+1];
	//file_char = filename.c_str();
	std::ifstream leveldata;
	leveldata.open(filename);
	int a, b, c;
	int index = 0;
	while(!leveldata.eof() && index < 100)
	{
		index++;
		leveldata >> a >> b >> c;
		type_p.push_back(b);
		endzone.push_back(c);
		final = a;
	}
}

//End of Board class

//Start of Player class:

Player::Player()
{
	position = 0;
	turns = 0;
	lad_up = 0;
	lad_down = 0;
	total_dice = 0;
	ladderstatus = 0;

}

void Player::Move(int newpos, int dice)
{
	position = newpos;
	turns += 1;
	total_dice += dice;
	ladderstatus = 0;
}

void Player::LadderUp()
{
	lad_up += 1;
	ladderstatus = 1;
}

void Player::LadderDown()
{
	lad_down += 1;
	ladderstatus = 2;
}

int Player::GetAverageDice()
{
	float average = total_dice/turns;
	return average;
}

void Player::Update(int player, Board * newboard, int steps)
{
	int near_up = 0;
	int near_down = 0;
	int final = newboard->GetLength();
	std::vector<int> type_p = newboard->GetType();
	for(int i = position; i<final; i++)
	{
		if ((near_up == 0) && (type_p[i] == 1))
		{
			near_up = i;
		}
		if ((near_down == 0) && (type_p[i] == 2))
		{
			near_down = i;
		}
	}

	std::cout << "\n\nPlayer " << player << ":";
	std::cout << " You rolled a " << steps << ", you are now on zone ";
	std::cout << position;

	if (near_up != 0)
	{
		std::cout << "\nThe nearest upwards ladder is at zone ";
		std::cout << near_up;
	}

	if (near_down != 0)
	{
		std::cout << "\nThe nearest downward ladder is at zone ";
		std::cout << near_down;
	}

	if (ladderstatus == 1)
	{
		std::cout << "\nYou went up a ladder! \n";
	}

	if (ladderstatus == 2)
	{
		std::cout << "\nyou went down a ladder! \n";
	}
}
