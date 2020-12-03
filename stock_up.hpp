#pragma once

#include <cpr/cpr.h>
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <fstream>

namespace bigm
{
    class stock_up
    {
    private:
        std::vector<int> nums;

    public:
        stock_up();
        std::vector<int> getMeStocks();


    };
}
