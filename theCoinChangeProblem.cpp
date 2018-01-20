long getWays(long n, vector < long > c){
    if(n < 0)
        return 0;
    if(n == 0)
        return 1;
    vector<long> amounts(n+1, 0);
    amounts[0] = 1;
    
    for(int c_i = 0; c_i < c.size(); c_i++){
        for(int a_i = 0; a_i < n+1; a_i++){
            if(a_i >= c[c_i])
                amounts[a_i] += amounts[a_i-c[c_i]];
        }
    }
    
    return amounts[n];
}