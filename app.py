import streamlit as st
total = 0
st.title("Restaurant")
prices={"Pizza🍕":8,"Pasta🍝":7,"Burger🍔":6,"Sandwich🥪":5,"Soup":4}
name=st.text_input("What is the name of the order")
phone=st.text_input("Please enter your phone number")
food=st.radio("Choose your favorite food",["Pizza🍕","Pasta🍝","Burger🍔","Sandwich🥪"])
quantity=st.number_input("Enter the amount of items")
pay=st.radio("Cash or Card?",["Cash💵","Card💳"])
st.write(quantity)
fries=st.checkbox("Fries")
cheese=st.checkbox("Cheese")
gb=st.checkbox("Garlic Bread")
ice_c=st.checkbox("Ice Cream")
if st.button("Submit Order"):
    st.write(food)
    st.write("Select the toppings")
    if cheese:
        st.write("Cheese🧀-1$")
        total=total+1
    if fries:
        st.write("Fries🍟-3$")
        total=total+3
    if gb:
        st.write("Garlic Bread🧄🥖-2$")
        total=total+2
    if ice_c:
        st.write("Ice Cream🍨-4$")
        total=total+4
    st.write(name)
    st.write(phone)
    st.write("Items Ordered")
    item_total = quantity * prices[food]
    total = total + item_total
    st.subheader(f"The total bill will be ${total}💵")
    st.write("Payment Method=" , pay , ".")


