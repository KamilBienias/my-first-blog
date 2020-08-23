from django.shortcuts import render, redirect
from .models import HostAndMask
from .forms import HostAndMaskForm


def pass_method(request):
    form = HostAndMaskForm(
        request.POST or None)  # jeśli metoda POST to renderuj ten formularz a jeśli nie ma danych to renderuj pusty formularz
    if form.is_valid():
        form.save(commit=True)
        # form = HostAndMaskForm()  # odświeża formularz, po zapisaniu będą puste pola. To już niepotrzebne, bo po wysłaniu przenosi na inną stronę
        return redirect("/ip/solution_ip")
    context = {
        'form': form
    }
    return render(request, "ipcalculator/pass_host_mask.html", context)


def solution_method(request):
    searches = HostAndMask.objects.all()
    searches_ids = []
    for search in searches:
        searches_ids.append(search.id)

    # take last one data from database
    added_search = HostAndMask.objects.get(id=searches_ids[-1])

    # change decimal digit into binary digit. If binary digit has less than 8 digits, then fill it by 0
    host_octet_1_binary_string = bin(int(added_search.host_octet_1))[2:].rjust(8, '0')
    host_octet_2_binary_string = bin(int(added_search.host_octet_2))[2:].rjust(8, '0')
    host_octet_3_binary_string = bin(int(added_search.host_octet_3))[2:].rjust(8, '0')
    host_octet_4_binary_string = bin(int(added_search.host_octet_4))[2:].rjust(8, '0')

    mask_octet_1_binary_string = bin(int(added_search.mask_octet_1))[2:].rjust(8, '0')
    mask_octet_2_binary_string = bin(int(added_search.mask_octet_2))[2:].rjust(8, '0')
    mask_octet_3_binary_string = bin(int(added_search.mask_octet_3))[2:].rjust(8, '0')
    mask_octet_4_binary_string = bin(int(added_search.mask_octet_4))[2:].rjust(8, '0')

    # calculate network address
    network_octet_1_binary_string = ""
    network_octet_2_binary_string = ""
    network_octet_3_binary_string = ""
    network_octet_4_binary_string = ""
    for i in range(8):
        network_octet_1_binary_string += str(min(host_octet_1_binary_string[i], mask_octet_1_binary_string[i]))
        network_octet_2_binary_string += str(min(host_octet_2_binary_string[i], mask_octet_2_binary_string[i]))
        network_octet_3_binary_string += str(min(host_octet_3_binary_string[i], mask_octet_3_binary_string[i]))
        network_octet_4_binary_string += str(min(host_octet_4_binary_string[i], mask_octet_4_binary_string[i]))

    # change binary strings into integers
    network_octet_1 = int(network_octet_1_binary_string, 2)
    network_octet_2 = int(network_octet_2_binary_string, 2)
    network_octet_3 = int(network_octet_3_binary_string, 2)
    network_octet_4 = int(network_octet_4_binary_string, 2)

    # NOT mask
    not_mask_octet_1_binary_string = ""
    not_mask_octet_2_binary_string = ""
    not_mask_octet_3_binary_string = ""
    not_mask_octet_4_binary_string = ""
    for i in range(8):
        not_mask_octet_1_binary_string += str((int(mask_octet_1_binary_string[i]) + 1) % 2)
        not_mask_octet_2_binary_string += str((int(mask_octet_2_binary_string[i]) + 1) % 2)
        not_mask_octet_3_binary_string += str((int(mask_octet_3_binary_string[i]) + 1) % 2)
        not_mask_octet_4_binary_string += str((int(mask_octet_4_binary_string[i]) + 1) % 2)

    # change binary strings into integers
    not_mask_octet_1 = int(not_mask_octet_1_binary_string, 2)
    not_mask_octet_2 = int(not_mask_octet_2_binary_string, 2)
    not_mask_octet_3 = int(not_mask_octet_3_binary_string, 2)
    not_mask_octet_4 = int(not_mask_octet_4_binary_string, 2)

    # calculate broadcast address
    broadcast_octet_1 = network_octet_1 + not_mask_octet_1
    broadcast_octet_2 = network_octet_2 + not_mask_octet_2
    broadcast_octet_3 = network_octet_3 + not_mask_octet_3
    broadcast_octet_4 = network_octet_4 + not_mask_octet_4

    # count amount of "1" in mask
    amount_of_1_in_mask_octet_1 = mask_octet_1_binary_string.count("1")
    amount_of_1_in_mask_octet_2 = mask_octet_2_binary_string.count("1")
    amount_of_1_in_mask_octet_3 = mask_octet_3_binary_string.count("1")
    amount_of_1_in_mask_octet_4 = mask_octet_4_binary_string.count("1")
    amount_of_1_in_mask = amount_of_1_in_mask_octet_1 + \
                          amount_of_1_in_mask_octet_2 + \
                          amount_of_1_in_mask_octet_3 + \
                          amount_of_1_in_mask_octet_4

    number_of_hosts = 2**(32-amount_of_1_in_mask)-2

    context = {
        'added_search': added_search,
        'network_octet_1': network_octet_1,
        'network_octet_2': network_octet_2,
        'network_octet_3': network_octet_3,
        'network_octet_4': network_octet_4,
        'broadcast_octet_1': broadcast_octet_1,
        'broadcast_octet_2': broadcast_octet_2,
        'broadcast_octet_3': broadcast_octet_3,
        'broadcast_octet_4': broadcast_octet_4,
        'amount_of_1_in_mask': amount_of_1_in_mask,
        'number_of_hosts': number_of_hosts
    }

    return render(request, "ipcalculator/solution.html", context)
