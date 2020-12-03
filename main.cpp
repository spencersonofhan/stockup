#include "stock_up.hpp"

int main()
{
    std::fstream file;
    std::vector<std::string> stockInfo;

    file.open("bought.csv", std::ios::in);

    // Check if file is actually open
    if (file.is_open())
    {
        std::string line;
        while(getline(file, line))
        {
            stockInfo.push_back(line);
        }

        file.close();
    }
    else
    {
        std::cout << "File did not open properly!" << std::endl;
        return 0;
    }

    std::cout << stockInfo[0] << std::endl;


    return 0;
}
