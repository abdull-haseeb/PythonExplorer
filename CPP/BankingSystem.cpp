#include <iostream>
#include <string>
#include <vector>

class BankAccount
{
protected:
    std::string accountNumber;
    double balance;

public:
    BankAccount(const std::string &accNum, double initialBalance)
        : accountNumber(accNum), balance(initialBalance) {}

    virtual void deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
            std::cout << "Deposited $" << amount << " into account " << accountNumber << std::endl;
        }
    }

    virtual void withdraw(double amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            std::cout << "Withdrawn $" << amount << " from account " << accountNumber << std::endl;
        }
        else
        {
            std::cout << "Insufficient balance in account " << accountNumber << std::endl;
        }
    }

    virtual void displayBalance() const
    {
        std::cout << "Account " << accountNumber << " balance: $" << balance << std::endl;
    }
};

class SavingsAccount : public BankAccount
{
    double interestRate;

public:
    SavingsAccount(const std::string &accNum, double initialBalance, double rate)
        : BankAccount(accNum, initialBalance), interestRate(rate) {}

    void applyInterest()
    {
        double interest = balance * interestRate / 100;
        balance += interest;
        std::cout << "Interest applied to account " << accountNumber << ": $" << interest << std::endl;
    }
};

int main()
{
    std::vector<BankAccount *> accounts;

    accounts.push_back(new BankAccount("12345", 1000));
    accounts.push_back(new SavingsAccount("54321", 1500, 2.5));

    for (BankAccount *account : accounts)
    {
        account->deposit(500);
        account->withdraw(200);
        account->displayBalance();

        SavingsAccount *savingsAccount = dynamic_cast<SavingsAccount *>(account);
        if (savingsAccount)
        {
            savingsAccount->applyInterest();
        }

        delete account;
    }

    return 0;
}
