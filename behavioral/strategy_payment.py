from abc import ABC, abstractmethod
import os

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float, output_file=None) -> bool:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry_date: str, cvv: str):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
    
    def process_payment(self, amount: float, output_file=None) -> bool:
        message = f"Processing credit card payment of ${amount:.2f}\nCard: ****-****-****-{self.card_number[-4:]}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float, output_file=None) -> bool:
        message = f"Processing PayPal payment of ${amount:.2f}\nEmail: {self.email}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
        return True

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def process_payment(self, amount: float, output_file=None) -> bool:
        message = f"Processing cryptocurrency payment of ${amount:.2f}\nWallet: {self.wallet_address[:8]}...{self.wallet_address[-4:]}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)
        return True

class PaymentProcessor:
    def __init__(self):
        self._strategy = None
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def execute_payment(self, amount: float, output_file=None) -> bool:
        if not self._strategy:
            raise ValueError("Payment strategy not set")
        return self._strategy.process_payment(amount, output_file)

def demo_strategy(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/strategy_payment.txt", "w") as f:
        f.write("=== Strategy Pattern: Payment Processing ===\n\n")
        processor = PaymentProcessor()
        
        # Credit Card Payment
        f.write("1. Credit Card Payment:\n")
        credit_card = CreditCardPayment("1234567812345678", "12/25", "123")
        processor.set_payment_strategy(credit_card)
        processor.execute_payment(99.99, f)
        f.write("\n")
        
        # PayPal Payment
        f.write("2. PayPal Payment:\n")
        paypal = PayPalPayment("user@example.com")
        processor.set_payment_strategy(paypal)
        processor.execute_payment(149.50, f)
        f.write("\n")
        
        # Crypto Payment
        f.write("3. Crypto Payment:\n")
        crypto = CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        processor.set_payment_strategy(crypto)
        processor.execute_payment(299.99, f)
        f.write("\n")
        
        f.write("Strategy pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_strategy()