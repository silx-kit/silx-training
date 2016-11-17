# Question 1.

from silx.io.spectoh5 import convert
from silx.io.utils import h5ls

convert("data/oleg.dat", "data/oleg.h5", mode="w")
print(h5ls("data/oleg.h5"))


##########################################
# Question 2.

from silx.io.spectoh5 import write_spec_to_h5
from silx.io.utils import h5ls

# specifying a path causes the file to be open,
# then closed again after writing is done
write_spec_to_h5("data/spectrum.dat", "data/concat.h5",
                 h5path="/spectrum", mode="w")
write_spec_to_h5("data/oleg.dat", "data/concat.h5",
                 h5path="/oleg", mode="a")

# alternative way: use a file handle rather than a file path
# (you are responsible for opening/closing the file)
import h5py

output_file = h5py.File("data/concat.h5", mode="a")
write_spec_to_h5("data/spectrum.dat", output_file,
                 h5path="/spectrum", overwrite_data=True)
write_spec_to_h5("data/oleg.dat", output_file,
                 h5path="/oleg_2")

print(h5ls(output_file))

output_file.close()


##########################################
# Question 3.

from silx.io.spectoh5 import convert
from silx.io.utils import h5ls

create_ds_args = {"chunks": True,
                  "compression": "gzip"}

convert("data/oleg.dat", "data/oleg.h5", mode="w",
        create_dataset_args=create_ds_args)
print(h5ls("data/oleg.h5"))
