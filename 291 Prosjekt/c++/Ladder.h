// #ifndef LADDERGAME_H_ 
// #define LADDERGAME_H_
#include <vector>


class Board
{
private:

	//board():
	std::vector<int> type_p;
	std::vector<int> endzone;
	int final;
//char myStr[] = "text";


public:
	Board(char filename[] = "Leveldesign.level");
	~Board() {};
	std::vector<int> GetType(){return type_p;};
	std::vector<int> GetDestination(){return endzone;};
	int GetLength() {return final;};

};


class Player
{
private:
	//Variables:

	//Player():
	int position;
	int turns;
	int lad_up;
	int lad_down;
	int total_dice;
	int ladderstatus;

	// GetAveragedice():
	int averagedice;


public:
	Player();
	~Player(){};
	void Move(int newpos, int dice);
	void LadderUp();
	void LadderDown();
	int GetPos(){return position;};
	int GetTurns(){return turns;};
	int GetLadderUp(){return lad_up;};
	int GetLadderDown(){return lad_down;};
	int GetAverageDice();
	void Update(int player, Board *newboard, int steps);
	


};
// #endif 
