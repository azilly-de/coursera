// ***************************************************************************
// * coursera - Discrete Optimization
// * Programming Assignment - Knapsack
// * Andreas Zilly - Juni 2013 - Public Domain
// * KEINE Ueberprufung ob optimale Loesung!
// * Bei bestimmten Grenzfaellen KEINE optimale Loesung! HACK!
// ***************************************************************************
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#include <fstream>
#include <sstream>

#include <boost/dynamic_bitset.hpp>
#include <boost/foreach.hpp>

int main(int argc, char** argv)
{
    if(argc < 2)
        return -1;

    std::string fileName = argv[1];
    std::ifstream infile(fileName.c_str(), std::ifstream::in);

    std::string line;

    //erste Zeile einlesen:
    std::getline(infile, line);
    std::istringstream iss(line);

    int numItems;
    int capacity;
    iss >> numItems >> capacity;

    std::vector<int> currentCost(capacity+1, 0);
    std::vector<int> previousCost(capacity+1, 0);
    std::vector< boost::dynamic_bitset<> > selected(capacity+1, numItems);

    std::vector<int> values;
    std::vector<int> weights;

    // weitere Zeilen einlesen:
    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        int value, weight;

        if (!(iss >> value >> weight)) {
            break;
        }

        values.push_back(value);
        weights.push_back(weight);
    }

    if(values.size() != numItems || weights.size() != numItems) {
        std::cout << "Error readin " << fileName << std::endl;
        return -1;
    }

    for(int i=0; i<numItems; i++) {
        for(int W=0; W<=capacity; W++ ) {
            if(weights[i] > W) {
                currentCost[W] = previousCost[W];

            } else {
                int possibleCost = previousCost[W-weights[i]] + values[i];
                currentCost[W] =
                    std::max(previousCost[W], possibleCost);

                if(currentCost[W] == values[i]) {
                    selected[W].reset();
                    selected[W][i] = 1;

                } else if(currentCost[W] == possibleCost) {
                    selected[W] = selected[W-weights[i]];
                    selected[W][i] = 1;
                }
            }
        }

        previousCost = currentCost;
    }

    // Ausgabe:
    std::cout << currentCost[capacity] << " 0" << std::endl;
    for (boost::dynamic_bitset<>::size_type i = 0; i < selected.back().size(); ++i){
         std::cout << selected.back()[i] << " ";
    }

    return 0;
}
