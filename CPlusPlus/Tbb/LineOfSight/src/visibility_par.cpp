#include <cmath>
#include <iostream>
#include <iomanip>
#include <limits>
#include <tbb/tbb.h>
#include "terrain.h"

auto compute_visibility(const Terrain& terrain) {
    std::vector<bool> is_visible;
    is_visible.reserve(terrain.n());
    [[maybe_unused]] double max_angle = tbb::parallel_scan(
        tbb::blocked_range<size_t>(0, terrain.n()),
        -std::numeric_limits<double>::max(),
        [&](const tbb::blocked_range<size_t>& r, double max_angle, bool is_final_scan) -> double {
            for (size_t i = r.begin(); i != r.end(); ++i) {
                double angle = atan2(terrain.altitude(i), terrain.distance(i));
                if (is_final_scan)
                    is_visible[i] = angle > max_angle;
                if (angle > max_angle)
                    max_angle = angle;
            }
            return max_angle;
        },
        [](double a, double b) -> double { return std::max(a, b); }
    );
    return is_visible;
}

int main() {
    Terrain terrain(std::cin);
    auto is_visible = compute_visibility(terrain);
    std::cout << std::setprecision(5) << std::fixed;
    for (size_t i = 0; i < terrain.n(); ++i)
        std::cout << terrain.distance(i) << " " << is_visible[i] << "\n";
    return 0;
}
