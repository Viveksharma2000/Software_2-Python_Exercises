# Exercise 1

from flask import Flask, request, jsonify

app = Flask(__name__)

def get_prime_factors(n):
    """Get all prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_prime(num):
    """Check whether a number is prime or not"""
    if num < 2:
        return False
    factors = get_prime_factors(num)
    unique_factors = set(factors)
    for factor in unique_factors:
        count = factors.count(factor)
        if count > 1:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def prime_check(number):
    """Check whether a number is prime or not"""
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


# Exercise 2

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample Airport Database (in memory for simplicity)
airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EHDP": {"Name": "Dublin Airport", "Location": "Dublin"},
    # Add more airports here...
}

@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    """Get airport information by ICAO code"""
    if icoa_code in airport_database:
        return jsonify({"ICAO": icoa_code, "Name": airport_database[icoa_code]["Name"], "Location": airport_database[icoa_code]["Location"]})
    else:
        return jsonify({"Error": f"Airport not found for ICAO code {icao_code}"}), 404

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')