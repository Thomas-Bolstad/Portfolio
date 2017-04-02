#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <string>
#include <ctime>
#include "Ladder.h"
#include "Ladder.cpp"   //fjern når du kompilerer i g++, HUSK!

//srand(time(0));  husk å fiks seeden på random generatoren.

int initial()
{
	int players = 0;
	while ((players != 1) && (players != 2) && (players != 3) && (players != 4))
	{
		std::cout << "How many players do you want (1-4)? ";
		std::cin >> players; 
		std::cout << "\n";
	}
	return players;
}
	
void endresults(std::vector<Player *> players, std::vector<int> places)
{
	// vector containing the relevant position strings
	// perhaps change these into chars since they're constant and don't need manipulation...?
	
	std::vector<std::string> positions;
	positions.push_back("first");
	positions.push_back("second");
	positions.push_back("third");
	positions.push_back("fourth");


	int size_p = players.size();
	std::cout << size_p;
	for (int i = 0; i < size_p; i++)
	{
		//to make sure it doesn't crash.
		if (places.size() > 0)
		{
			int turns = players[places[i] - 1]->GetTurns();
			int lad_up = players[places[i] - 1]->GetLadderUp();
			int lad_down = players[places[i] - 1]->GetLadderDown();
			int avg_dice = players[places[i] - 1]->GetAverageDice();

			std::cout << "\n\nplayer " << places[i] << " ended in " << positions[i];
			std::cout << " place after " << turns << " turns. \n";
			std::cout << "And went up " << lad_up << " ladders, and down ";
			std::cout << lad_down << " ladders.\n";
			std::cout << "And threw in average " << avg_dice << " with the dice.";
		}
	}
	std::cout << "\n\npress \"Q\" to quit!";
	while(std::cin.get() != 'Q')
	{
		continue;
	}
}

char inputCheck()
{
	char choice = ' ';
	while ((choice != 'R') && (choice != 'Q') && (choice != 'L') && (choice != 'P'))
	{
		std::cout << "\n\nR for roll, L for ladders, P for positions, Q for quit: ";
		std::cin >> choice;

	}
	return choice;
}



void listzones(Board *newboard)
{
	std::vector<int> type = newboard->GetType();
	std::vector<int> endzone = newboard->GetDestination();
	int type_size = type.size();
	for (int i = 0; i < type_size; i++)
	{
		if (type[i] == 1)
		{
			std::cout << "\n\nUpward ladder at zone " << i << " which ends at zone ";
			std::cout << endzone[i] ;
		}
		if (type[i] == 2)
		{
			std::cout << "\n\nDownward ladder at zone " << i << " which ends at zone ";
			std::cout << endzone[i];
		}
	}
}

void cur_positions(std::vector<Player *> players)
{
	int size = players.size();
	std::cout << "\n\n";
	for (int i = 0; i < size; i++)
	{
		int position = players[i]->GetPos();
		std::cout << "Player " << i+1 << " is in zone " << position << "\n";
	}
}

bool playermove(int playnum, int roll, Player *cur_player, Board *cur_board)
{
	bool goal = false;
	int position = cur_player->GetPos();
	int newpos = position + roll;
	int final = cur_board->GetLength();
	if (newpos < final)
	{
		std::vector<int> zone_type = cur_board->GetType();
		std::vector<int> end = cur_board->GetDestination();
		if (zone_type[newpos] == 0)
		{
			cur_player->Move(newpos, roll);
		}
		else if (zone_type[newpos] == 1)
		{
			newpos = end[newpos];
			cur_player->Move(newpos, roll);
			cur_player->LadderUp();
		}
		else if (zone_type[newpos] == 2)
		{
			newpos = end[newpos];
			cur_player->Move(newpos, roll);
			cur_player->LadderDown();
		}
	}
	else
	{
		cur_player->Move(final, roll);
		goal = true;
	}
	int pos = cur_player->GetPos();
	return goal;
}

int Dice()
{
	int roll = rand() % 6 + 1;
	return roll;
}

std::vector<int> vect_remove(int value, std::vector<int> cur_vect)
{
	int v_size = cur_vect.size();
	std::vector<int> new_vect;
	for(int i = 0; i < v_size; i++)
	{
		if (cur_vect[i] != value)
		{
			new_vect.push_back(cur_vect[i]);
		}
	}
	return new_vect;
}

int main()
{
	int players = initial();
	std::vector<int> active;
	std::vector<int> all_players;
	std::vector<int> places;
	std::vector<Player *> play_class;
	for (int i = 0; i < players; i++)
	{
		Player *newplayer;
		newplayer = new Player();
		active.push_back(i + 1);
		all_players.push_back(i + 1);
		play_class.push_back(newplayer);
	}
	Board *newboard;
	newboard= new Board();
	bool playing = true;
	while (playing == true)
	{
		int index = 0;
		while (index < active.size())
		{
			int cur_p = active[index];
			char choice = inputCheck();
			if (choice == 'R')
			{
				int roll = Dice();
				bool goal = playermove(index + 1, roll, play_class[cur_p - 1], newboard);
				play_class[cur_p - 1]->Update(cur_p, newboard, roll);
				if (goal == true)
				{
					places.push_back(cur_p);
					active = vect_remove(cur_p, active);
					std::cout << "\nPlayer " << cur_p << "reached the goal!\n";
				}
				else
				{
					index++;
				}
			}
			else if (choice == 'L')
			{
				listzones(newboard);
			}
			else if (choice == 'P')
			{
				cur_positions(play_class);
			}
			else if (choice  == 'Q')
			{
				playing = false;
				break;
			}
		}
		if (active.size() == 0)
		{
			playing = false;
			active.clear();
		}
	}
	endresults(play_class, places);
return 0;
}
