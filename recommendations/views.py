# recommendations/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile, Service
from .forms import ServiceSearchForm

#def recommended_services(request):
#    services = Service.objects.all()
#    return render(request, 'recommendations/recommended_services.html', {'services': services})
from .models import FinancialService

def topic_search(request):
    form = ServiceSearchForm(request.GET)
    services = FinancialService.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        if search_query:
            services = services.filter(name__icontains=search_query)

    return render(request, 'recommendations/topic_search.html', {'form': form, 'services': services})



def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'recommendations/service_detail.html', {'service': service})

def recommended_services(request):
    services_list = [
        'Savings Account',
        'Checking Account',
        'Personal Loan',
        'Mortgage',
        'Auto Loan',
        'Credit Card',
        'Brokerage Account',
        'Mutual Funds',
        'Retirement Accounts',
        'Internet Banking',
        'Mobile Banking',
        'ATM Services',
        'Wire Transfers',
        'Online Bill Payment',
        'Insurance Services',
        'Risk Assessment',
        'Currency Exchange',
        'Business Loans',
        'Merchant Services',
        'Business Accounts',
        'Wealth Management',
        'Financial Advisory',
        'Safe Deposit Boxes',
        'Overdraft Protection',
        'Escrow Services',
        'Notary Services',
        'Financial Education and Counseling',
        'Mobile Wallets',
        'Peer-to-Peer (P2P) Payments',
        'Currency and Coin Services',
        'Electronic Funds Transfer',
        'Fraud Protection Services',
        'Financial Software Integration',
        'Customer Rewards Programs',
        'Documentary Collections',
        'Foreign Currency Accounts',
        'Trust and Estate Planning Services',
        'Cash Management Services',
        'Remote Deposit Capture',
        'Prepaid Cards',
        'Small Business Services',
        'Custodial Services',
        'Student Loans',
        'Health Savings Accounts',
        'ATM Fee Reimbursement',
        'Personal Financial Management Tools',
        'Lines of Credit',
        'Certificate of Deposit (CD)',
        'Student Checking Accounts',
        'Green Banking Initiatives',
        'Financial Workshops and Seminars',
        'Charitable Giving Accounts',
        'Online Loan Applications',
        'Travel Insurance',
        'Home Equity Lines of Credit (HELOC)',
        'Debt Consolidation Loans',
        'Individual Development Accounts (IDAs)',
        'Automated Investment Services (Robo-Advisors)',
        'Flexible Spending Accounts (FSAs)',
        'Business Line of Credit',
        'Virtual Account Management',
        'Cryptocurrency Services',
        'Ethical Investing Solutions',
        'Real Estate Financing Consultation'
    ]

    return render(request, 'recommendations/services.html', {'services_list': services_list})

