#include <bits/stdc++.h> 
using namespace std;
int main()
{
vector<string> NonT = {"S", "NP", "VP", "N", "V", "P", "PN", "D"}; vector<string> Ter =
{ "chahelpionship", "ball", "toss", "is", "want", "won", "played", "me", "i",
"you", "india", "australia "," steve "," john "," the "," a "," an "}; int n = NonT.size();
int m = Ter.size();
map<string, map<string, vector<string>>> help;

for (auto i : NonT)
{
for (auto j : Ter)
{
help[i][j] = {""};
}
}
help["S"]["is"] = {"NP", "VP"};
help["S"]["want"] = {"NP", "VP"};
help["S"]["won"] = {"NP", "VP"};
help["S"]["played"] = {"NP", "VP"};
help["S"]["me"] = {"NP", "VP"};
help["S"]["i"] = {"NP", "VP"};
help["S"]["you"] = {"NP", "VP"};
help["S"]["india"] = {"NP", "VP"};
help["S"]["australia"] = {"NP", "VP"};
help["S"]["steve"] = {"NP", "VP"};
help["S"]["john"] = {"NP", "VP"};
help["S"]["the"] = {"NP", "VP"};
help["S"]["a"] = {"NP", "VP"};
help["S"]["an"] = {"NP", "VP"};
help["NP"]["me"] = {"P"};
help["NP"]["i"] = {"P"};
help["NP"]["you"] = {"P"};
help["NP"]["india"] = {"PN"};
help["NP"]["australia"] = {"PN"};
help["NP"]["steve"] = {"PN"};
help["NP"]["john"] = {"PN"};
help["NP"]["the"] = {"D", "N"};
help["NP"]["a"] = {"D", "N"};
help["NP"]["an"] = {"D", "N"};
help["VP"]["is"] = {"V", "NP"};
help["VP"]["want"] = {"V", "NP"};
help["VP"]["won"] = {"V", "NP"};
help["VP"]["played"] = {"V", "NP"};
help["N"]["chahelpionship"] = {"chahelpionship"};
help["N"]["ball"] = {"ball"};
help["N"]["toss"] = {"toss"};
help["V"]["is"] = {"is"};
help["V"]["want"] = {"want"};
help["V"]["won"] = {"won"};
help["V"]["played"] = {"played"};
help["P"]["me"] = {"me"};
help["P"]["i"] = {"i"};
help["P"]["you"] = {"you"};
help["PN"]["india"] = {"india"};
help["PN"]["australia"] = {"australia"};
help["PN"]["steve"] = {"steve"};
help["PN"]["john"] = {"john"};
help["D"]["the"] = {"the"};
help["D"]["a"] = {"a"};
help["D"]["an"] = {"an"};

vector<string> input = {"india", "won", "the", "chahelpionship"};
 stack<string> buffer;
stack<string> st; buffer.push("$");
for (int i = input.size() - 1; i >= 0; i--)
{
buffer.push(input[i]);
}
st.push("$");
st.push("S"); 
cout << "Buffer"
<< " -- "
<< "Stack\n\n"; int loop = 10000; while (loop--)
{
if (buffer.size() == 0 && st.size() == 0)
{
cout << "\n\nString Valid" << endl; return 0;
}
if (buffer.size() == 0 || st.size() == 0)

{
cout << "\n\nString Invalid" << endl; return 0;
}
string s1 = buffer.top(); string s2 = st.top();
cout << s1 << " -- " << s2 << endl; if (s1 == "" || s1 == "#")
{
buffer.pop(); continue;
}
if (s2 == "" || s2 == "#")
{
st.pop(); continue;
}
if (s1 == s2)
{
buffer.pop();
st.pop(); continue;
}
vector<string> v = help[s2][s1]; reverse(v.begin(), v.end()); st.pop();
for (auto i : v)
{
st.push(i);
}
}
cout << "Invalid" << endl; return 0;
}


