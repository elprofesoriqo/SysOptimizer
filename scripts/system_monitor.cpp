#include <windows.h>
#include <psapi.h>
#include <json/json.h>
#include <fstream>

int main() {
    DWORD processes[1024], cbNeeded, cProcesses;
    EnumProcesses(processes, sizeof(processes), &cbNeeded);
    cProcesses = cbNeeded / sizeof(DWORD);

    Json::Value root;
    for (unsigned int i = 0; i < cProcesses; i++) {
        DWORD processID = processes[i];
        HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, processID);

        if (hProcess) {
            HMODULE hMod;
            DWORD cbNeeded;
            char szProcessName[MAX_PATH] = "<unknown>";

            if (EnumProcessModules(hProcess, &hMod, sizeof(hMod), &cbNeeded)) {
                GetModuleBaseNameA(hProcess, hMod, szProcessName, sizeof(szProcessName));
            }

            PROCESS_MEMORY_COUNTERS pmc;
            if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
                Json::Value process;
                process["pid"] = processID;
                process["name"] = szProcessName;
                process["memory_usage_kb"] = static_cast<Json::UInt64>(pmc.WorkingSetSize / 1024);
                root.append(process);
            }
            CloseHandle(hProcess);
        }
    }

    std::ofstream file("processes.json");
    file << root.toStyledString();
    file.close();

    return 0;
}
