var bisect_left = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = ~~((i + j) / 2);
        if (nums[mid] < target)
            i = mid + 1;
        else
            j = mid;
    }
    return i;
}

var bisect_right = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = Math.ceil((i + j) / 2);
        if (nums[mid] > target)
            j = mid - 1;
        else
            i = mid;
    }
    return j;
}

var two_d_array = function(m, n) {
    return new Array(m).fill(0).map(() => new Array(n).fill(0));
}

var reverse = function(s) {
    return [...str].reverse().join('');
}


// simple print
var print = function(a) {
    console.log(a);
}

// For counting elements in a list 
var counter = function(array_or_string) {
    var dict = {};
    for (let i = 0; i < array_or_string.length; i++) {
        let e = array_or_string[i];
        dict[e] = dict[e] ? dict[e] += 1 : 1;
    }
    return dict;
}

var sum = function(array) {
    return array.reduce(function(a, b) {
        return a + b;
    }, 0);
}

var isodd = function(n) {
    return n % 2 == 1;
}

var iseven = function(n) {
    return n % 2 == 0;
}

var list = function(size, value) {
    return Array(size).fill(value);
}


var len = function(str_or_array) {
    return str_or_array.length;
}

var sorted = function(arr) {
    return arr.sort((a, b) => (a - b));
}

var sort_by_last = function(arr){
    return arr.sort((a, b)=>(last(a) - last(b)));
}

var sort_by_first = function(arr){
    return arr.sort((a, b)=>(a[0] - b[0]));
}

// print out a Map 
function printMap(m) {
    m.forEach(function(v, k) {
        console.log(k + " " + v);
    })
}

var gcd = function(a, b) {
    return b == 0 ? a : gcd(b, a % b);
}

var say = function(a) {
    console.log(a)
};


var two_d_array = function(m, n, v = 0) {
    return [...Array(m)].map(x => Array(n).fill(v));
}

function floor(float_number) {
    return Math.floor(float_number)
}

function ceil(float_number) {
    return Math.ceil(float_number)
}


var max = function(arr) {
    return Math.max(...arr);
}

var min = function(arr) {
    return Math.min(...arr)
};

var pairmax = function(a, b) {
    return Math.max(a, b)
}

var pairmin = function(a, b) {
    return Math.min(a, b)
}

// create an array with elements from 0 to n
var nlist = function(n) {
    return [...Array(n + 1).keys()];
}

var ispalindrome = function(s) {
    var i = 0,
        j = len(s) - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i += 1;
        j -= 1;
    }
    return true;
}

function permutations(inputArr) {
    var results = [];

    function permute(arr, memo) {
        var cur, memo = memo || [];

        for (var i = 0; i < arr.length; i++) {
            cur = arr.splice(i, 1);
            if (arr.length === 0) {
                results.push(memo.concat(cur));
            }
            permute(arr.slice(), memo.concat(cur));
            arr.splice(i, 0, cur[0]);
        }

        return results;
    }

    return permute(inputArr);
}

var directions = [
    [-1, -1],
    [-1, 1],
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, -1],
    [1, 0],
    [1, 1]
]

var inf = Infinity;

var last = function(arr) {
    return arr[len(arr) - 1];
}

var first = function(arr) {
    return arr[0];
}

var second = function(arr) {
    return arr[1];
}

var third = function(arr) {
    return arr[2];
}

function exist(key, hash) {
    return (key in hash);
}

// shortest common super-sequence
var scs = function(s, t) {
    var m = len(s),
        n = len(t),
        dp = two_d_array(m + 1, n + 1);
    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++)
            if (s[i - 1] == t[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = pairmax(dp[i - 1][j], dp[i][j - 1]);

    var i = m,
        j = n,
        index = m + n - last(last(dp)),
        res = list(index, '*');

    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            res[index - 1] = s[i - 1];
            i -= 1;
            j -= 1;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            res[index - 1] = s[i - 1];
            i -= 1;
        } else {
            res[index - 1] = t[j - 1];
            j -= 1;
        }
        index -= 1;
    }


    if (i + j == 0) return res.join('');
    if (j > 0) {
        i = j;
        s = t;
    }

    while (i > 0) {
        res[index - 1] = s[i - 1];
        index -= 1;
        i -= 1;
    }
    return res.join('');
}

// longest common subsequence
var lcs = function(s, t) {
    var m = len(s),
        n = len(t),
        dp = two_d_array(m + 1, n + 1);
    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++)
            if (s[i - 1] == t[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = pairmax(dp[i - 1][j], dp[i][j - 1]);

    var i = m,
        j = n,
        index = last(last(dp)),
        res = list(index, '*');

    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            res[index - 1] = s[i - 1];
            index -= 1;
            i -= 1;
            j -= 1;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i -= 1;
        } else {
            j -= 1;
        }
    }
    return res.join('');
}


var zip = function(lista, listb) {
    return a.map(function(e, i){return [e, b[i]];});
}

class Counter {
    constructor() {
        this.m = {};
    }

    read(key) {
        return exist(key, this.m) ? this.m[key] : 0;
    }

    plusone(key) {
        if (!this.m[key]) this.m[key] = 0;
        this.m[key] += 1;
    }
}


var div = function(n, k) { return floor(n / k); }

// inclusive of both endpoints
var randint = function(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}




/*
 * @lc app=leetcode id=1109 lang=javascript
 *
 * [1109] Corporate Flight Bookings
 *
 * https://leetcode.com/problems/corporate-flight-bookings/description/
 *
 * algorithms
 * Medium (45.07%)
 * Total Accepted:    4.4K
 * Total Submissions: 9.6K
 * Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
 *
 * There are n flights, and they are labeled from 1 to n.
 * 
 * We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k]
 * means that we booked k seats from flights labeled i to j inclusive.
 * 
 * Return an array answer of length n, representing the number of seats booked
 * on each flight in order of their label.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
 * Output: [10,55,45,25,25]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= bookings.length <= 20000
 * 1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
 * 1 <= bookings[i][2] <= 10000
 * 
 */
/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
var corpFlightBookings = function(bookings, n) {
    
};
