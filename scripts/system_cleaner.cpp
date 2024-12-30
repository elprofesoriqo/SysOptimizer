#include <windows.h>
#include <json/json.h>
#include <fstream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    std::string tempPath = getenv("TEMP");
    Json::Value root;
    Json::Value deletedFiles(Json::arrayValue);

    try {
        for (const auto& entry : fs::directory_iterator(tempPath)) {
            if (fs::is_regular_file(entry)) {
                deletedFiles.append(entry.path().string());
                fs::remove(entry);
            }
        }
        root["status"] = "success";
    } catch (const std::exception& e) {
        root["status"] = "error";
        root["message"] = e.what();
    }

    root["deleted_files"] = deletedFiles;

    std::ofstream file("clean_report.json");
    file << root.toStyledString();
    file.close();

    return 0;
}
